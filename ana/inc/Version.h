#ifndef   VERSION_H
#define   VERSION_H

# ifdef __cplusplus
extern "C" {
# endif

#define GIT_BRANCH      "master"      /*! Current name of the branch     */
#define GIT_COMMIT_HASH "b17a8cd" /*! Current hash of the git branch */
#define GIT_DATE        "2017-12-07 18:58:09 +0100" /*! Current date of the git branch */
#define GIT_TAG         "v0.0.31-18-gb17a8cd"         /*! Current tag of the git branch  */

#if DEBUG
#define CONF_MODE       "DEBUG" /*! Last compilation mode used */
#else
#define CONF_MODE       "RELEASE"/*! Last compilation mode used */
#endif

#define META_INFO       "master - v0.0.31-18-gb17a8cd - b17a8cd - 2017-12-07 18:58:09 +0100 - "CONF_MODE /*! Version name */

# ifdef __cplusplus
}
# endif

#endif //VERSION_H
