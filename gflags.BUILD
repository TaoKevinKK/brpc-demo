cc_library(
    name = "gflags",
    srcs = [
        "src/gflags.cc",
        "src/gflags_completions.cc",
        "src/gflags_reporting.cc",
        "src/mutex.h",
        "src/util.h",
        ":config_h",
        ":gflags_completions_h",
        ":gflags_declare_h",
        ":gflags_h",
        ":includes",
    ],
    hdrs = ["gflags.h"],
    copts = [
        # The config.h gets generated to the package directory of
        # GENDIR, and we don't want to put it into the includes
        # otherwise the dependent may pull it in by accident.
        "-I$(GENDIR)/" + PACKAGE_NAME,
        "-Wno-sign-compare",
        "-DHAVE_STDINT_H",
        "-DHAVE_SYS_TYPES_H",
        "-DHAVE_INTTYPES_H",
        "-DHAVE_SYS_STAT_H",
        "-DHAVE_UNISTD_H",
        "-DHAVE_FNMATCH_H",
        "-DHAVE_STRTOLL",
        "-DHAVE_STRTOQ",
        "-DHAVE_PTHREAD",
        "-DHAVE_RWLOCK",
        "-DGFLAGS_INTTYPES_FORMAT_C99",
    ],
    includes = [
        "include",
    ],
    visibility = ["//visibility:public"],
)