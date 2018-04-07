#ifndef PyAdaBoost_H
#define PyAdaBoost_H

#include "Python.h"
#include "numpy/arrayobject.h"

#include "TString.h"

#include <string>
#include <exception>


class PyGILRAII {
   PyGILState_STATE m_GILState;
public:
   PyGILRAII():m_GILState(PyGILState_Ensure()){}
   ~PyGILRAII(){PyGILState_Release(m_GILState);}
};

#ifndef PyObject_HEAD
struct _object;
typedef _object PyObject;
#define Py_single_input 256
#endif

struct PyArrayObject;

using namespace std;

class PyAdaBoost{
    public:
        PyAdaBoost() = delete;
        PyAdaBoost(const string& filename) {
            Py_Initialize();
            PyGILRAII thePyGILRAII;
            _import_array();
            fMain = PyImport_AddModule("__main__");
            fGlobalNS = PyModule_GetDict(fMain);
            PyObject *bName =  PyUnicode_FromString("__builtin__");
            // Import the file as a Python module.
            fModuleBuiltin = PyImport_Import(bName);

            fLocalNS = PyDict_New();

            PyObject *mDict = PyModule_GetDict(fModuleBuiltin);
            fEval = PyDict_GetItemString(mDict, "eval");
            fOpen = PyDict_GetItemString(mDict, "open");
            Py_DECREF(bName);
            Py_DECREF(mDict);

            PyObject *pName = PyUnicode_FromString("pickle");
            // Import the file as a Python module.
            fModulePickle = PyImport_Import(pName);
            PyObject *pDict = PyModule_GetDict(fModulePickle);
            fPickleDumps = PyDict_GetItemString(pDict, "dump");
            fPickleLoads = PyDict_GetItemString(pDict, "load");
            Py_DECREF(pName);
            Py_DECREF(pDict);

            PyRunString("import sklearn.ensemble");

            // Load file
            PyObject *file_arg = Py_BuildValue("(ss)", filename.c_str(),"rb");
            PyObject *file = PyObject_CallObject(fOpen,file_arg);
            if(!file) {
                cerr << "Ouch-Ouch! I can't open the file: " << filename << std::endl;
                throw runtime_error("Python pickle file read error");
            }

            // Load object from file using pickle
            PyObject *model_arg = Py_BuildValue("(O)", file);
            fClassifier = PyObject_CallObject(fPickleLoads , model_arg);
            if(!fClassifier) {
                cerr << "Cannot instantiate classifier" << endl;
                throw runtime_error("Python classifier instantiation error");
            }

            Py_DECREF(file_arg);
            Py_DECREF(file);
            Py_DECREF(model_arg);

            // Book classifier object in python dict
            PyDict_SetItemString(fLocalNS, "classifier", fClassifier);

            if(fClassifier){
                dims[0] = 1;
                dims[1] = fNvars;
            }
        }
        void PyRunString(TString code, TString errorMessage="Failed to run python code", int start=Py_single_input) {
            auto fPyReturn = PyRun_String(code, start, fGlobalNS, fLocalNS);
            if (!fPyReturn) {
                std::cout << "Failed to run python code: " << code << std::endl;
                std::cout << "Python error message:" << std::endl;
                PyErr_Print();
            }
        };
        float getMVA(const vector<float>& ar) {
               PyArrayObject *pEvent= (PyArrayObject *)PyArray_SimpleNew(2, dims, NPY_FLOAT);
                float *pValue = (float *)(PyArray_DATA(pEvent));
                for (UInt_t i = 0; i < fNvars; i++) pValue[i] = ar[i];

                // Get prediction from classifier
                PyArrayObject *result = (PyArrayObject *)PyObject_CallMethod(fClassifier, const_cast<char *>("decision_function"), const_cast<char *>("(O)"), pEvent);
                double *proba = (double *)(PyArray_DATA(result));

                // Return MVA value
                Double_t mvaValue;
                mvaValue = proba[0]; // getting signal probability
                // for(auto el: ar) std::cout << el << ", " ;
                // std::cout << std::endl;
                // std::cout <<  "BDT: " << mvaValue << std::endl;

                Py_DECREF(result);
                Py_DECREF(pEvent);
                return mvaValue;
        }
        virtual ~PyAdaBoost() {}

 private:
        // NOTE: Introduce here nothing that breaks if multiple instances
        // of the same method share these objects, e.g., the local namespace.
        PyObject *fModuleBuiltin = NULL;
        PyObject *fEval = NULL;
        PyObject *fOpen = NULL;

        PyObject *fModulePickle = NULL;
        PyObject *fPickleDumps = NULL;
        PyObject *fPickleLoads = NULL;

        PyObject *fMain = NULL;
        PyObject *fGlobalNS = NULL;
        PyObject *fLocalNS = NULL;

        PyObject *fClassifier; // Classifier object
        PyObject *fPyReturn; // python return data

        // NOTE: This has to be repeated here for the reader application
        const int fNvars = 16;
        const int fNoutputs = 2;
        npy_intp dims[2];
};

#endif //PyAdaBoost_H