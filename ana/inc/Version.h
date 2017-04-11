#ifndef   VERSION_H
#define   VERSION_H

# ifdef __cplusplus
extern "C" {
# endif

#define GIT_BRANCH      "master"      /*! Current name of the branch     */
#define GIT_COMMIT_HASH "71ed416" /*! Current hash of the git branch */
#define GIT_DATE        "2017-03-30 00:12:39 +0200" /*! Current date of the git branch */
#define GIT_TAG         "v0.0.15patch1-8-g71ed416"         /*! Current tag of the git branch  */

#if DEBUG
#define CONF_MODE       "DEBUG" /*! Last compilation mode used */
#else
#define CONF_MODE       "RELEASE"/*! Last compilation mode used */
#endif

#define META_INFO       "master - v0.0.15patch1-8-g71ed416 - 71ed416 - 2017-03-30 00:12:39 +0200 - "CONF_MODE /*! Version name */

# ifdef __cplusplus
}
# endif

#endif //VERSION_H
