#ifndef   VERSION_H
#define   VERSION_H

# ifdef __cplusplus
extern "C" {
# endif

#define GIT_BRANCH      "v43ttccsplit"      /*! Current name of the branch     */
#define GIT_COMMIT_HASH "bf6a7bc" /*! Current hash of the git branch */
#define GIT_DATE        "2019-07-30 17:35:24 +0200" /*! Current date of the git branch */
#define GIT_TAG         "v0.0.43ttccsplit-1-gbf6a7bc"         /*! Current tag of the git branch  */

#if DEBUG
#define CONF_MODE       "DEBUG" /*! Last compilation mode used */
#else
#define CONF_MODE       "RELEASE"/*! Last compilation mode used */
#endif

#define META_INFO       "v43ttccsplit - v0.0.43ttccsplit-1-gbf6a7bc - bf6a7bc - 2019-07-30 17:35:24 +0200 - "CONF_MODE /*! Version name */

# ifdef __cplusplus
}
# endif

#endif //VERSION_H
