load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "com_google_protobuf",
    sha256 = "9748c0d90e54ea09e5e75fb7fac16edce15d2028d4356f322176223f8ef46f46",
    strip_prefix = "protobuf-3.20.0",
    urls = ["https://github.com/protocolbuffers/protobuf/archive/v3.20.0.tar.gz"],
)

http_archive(
    name = "com_github_gflags_gflags",
    strip_prefix = "gflags-46f73f88b18aee341538c0dfc22b1710a6abedef",
    url = "https://github.com/gflags/gflags/archive/46f73f88b18aee341538c0dfc22b1710a6abedef.tar.gz",
)

bind(
    name = "gflags",
    actual = "@com_github_gflags_gflags//:gflags",
)

http_archive(
    name = "com_github_google_leveldb",
    build_file = "//:depBUILD/leveldb.BUILD",
    strip_prefix = "leveldb-a53934a3ae1244679f812d998a4f16f2c7f309a6",
    url = "https://github.com/google/leveldb/archive/a53934a3ae1244679f812d998a4f16f2c7f309a6.tar.gz"
)

http_archive(
    name = "com_github_google_glog",
    build_file = "depBUILD/glog.BUILD",
    strip_prefix = "glog-a6a166db069520dbbd653c97c2e5b12e08a8bb26",
    url = "https://github.com/google/glog/archive/a6a166db069520dbbd653c97c2e5b12e08a8bb26.tar.gz"
)

http_archive(
    name = "com_google_googletest",
    strip_prefix = "googletest-0fe96607d85cf3a25ac40da369db62bbee2939a5",
    url = "https://github.com/google/googletest/archive/0fe96607d85cf3a25ac40da369db62bbee2939a5.tar.gz",
)

new_local_repository(
    name = "openssl",
    path = "/usr",
    build_file = "depBUILD/openssl.BUILD",
)

new_local_repository(
    name = "openssl_macos",
    build_file = "depBUILD/openssl.BUILD",
    path = "/usr/local/opt/openssl",
)

bind(
    name = "ssl",
    actual = "@openssl//:ssl"
)

bind(
    name = "ssl_macos",
    actual = "@openssl_macos//:ssl"
)

new_local_repository(
    name = "zlib",
    build_file = "depBUILD/zlib.BUILD",
    path = "/usr",
)
http_archive(
    name = "brpc",
    strip_prefix = "brpc-1.3.0",
    url = "https://github.com/apache/brpc/archive/refs/tags/1.3.0.tar.gz"
)

