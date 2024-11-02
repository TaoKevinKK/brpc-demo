# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

load("//bazel:ray.bzl", "COPTS")

# 运行指定的命令
COPTS = [
    "-D__STDC_FORMAT_MACROS",
    "-DBTHREAD_USE_FAST_PTHREAD_MUTEX",
    "-D__const__=",
    "-D_GNU_SOURCE",
    "-DUSE_SYMBOLIZE",
    "-DNO_TCMALLOC",
    "-D__STDC_LIMIT_MACROS",
    "-D__STDC_CONSTANT_MACROS",
    "-fPIC",
    "-Wno-unused-parameter",
    "-fno-omit-frame-pointer",
    "-DGFLAGS_NS=google",
]

# pb的编译
proto_library(
    name = "c++_http_proto",
    srcs = [
        "proto/http.proto",
    ],
)
# 将pb编译声明为一个依赖dep
cc_proto_library(
    name = "cc_c++_http_proto",
    deps = [
        ":c++_http_proto",
    ],
)

# pb的编译
proto_library(
    name = "c++_echo_proto",
    srcs = [
        "proto/echo.proto",
    ],
)
# 将pb编译声明为一个依赖dep
cc_proto_library(
    name = "cc_c++_echo_proto",
    deps = [
        ":c++_echo_proto",
    ],
)

cc_binary(
    name = "benchmark_server",
    srcs = [
        "benchmark_server.cpp",
    ],
    hdrs = [
        "brpc_client_sync.h",
        "continue_streaming.h",
        "util.h",
        "config.h",
    ],
    deps = [
        ":cc_c++_echo_proto",
        "@apache_brpc//:brpc",
        "@com_github_fmtlib_fmt//:fmtlib",
        "@com_github_google_glog//:glog",
    ],
    copts = COPTS,
)


cc_binary(
    name = "benchmark_client",
    srcs = [
        "benchmark_client.cpp",
    ],
    hdrs = [
        "brpc_client_sync.h",
        "continue_streaming.h",
        "util.h",
        "config.h",
    ],
    deps = [
        ":cc_c++_echo_proto",
        "@apache_brpc//:brpc",
        "@com_github_fmtlib_fmt//:fmtlib",
        "@com_github_google_glog//:glog",
    ],
    copts = COPTS,
)