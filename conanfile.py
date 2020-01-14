from conans import ConanFile, CMake, tools
from sys import platform
import re
import os


class LibzmqConan(ConanFile):
    name = "libzmq"
    version = "4.3.2"
    license = "GPL-3.0-only"
    url = "https://github.com/zeromq/libzmq.git"
    description = "The ZeroMQ lightweight messaging kernel is a library which extends the standard socket interfaces " \
                  "with features traditionally provided by specialised messaging middleware products. ZeroMQ sockets " \
                  "provide an abstraction of asynchronous message queues, multiple messaging patterns, message " \
                  "filtering (subscriptions), seamless access to multiple transport protocols and more."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "fPIC": [True, False],
               "libsodium": [True, False], }
    default_options = {"shared": True,
                       "fPIC": True,
                       "libsodium": False, }
    generators = "cmake"

    def requirements(self):
        if self.options.libsodium:
            self.requires("libsodium/1.0.18@conan/stable")

    def source(self):
        git = tools.Git()
        git.clone(self.url, "v%s" % self.version, shallow=True)

    def system_requirements(self):
        pass

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['WITH_LIBSODIUM'] = "ON" if self.options.libsodium else "OFF"
        cmake.configure(build_folder='cmake-build')
        return cmake

    def build(self):
        tools.replace_in_file("CMakeLists.txt", "project(ZeroMQ)",
                              '''project(ZeroMQ)
                            include(${CMAKE_CURRENT_SOURCE_DIR}/conanbuildinfo.cmake)
                            conan_basic_setup()''')
        env_build = self._configure_cmake()
        env_build.build()
        env_build.test()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        if self.options.shared:
            self.copy("*.so*", dst="lib", keep_path=False)
        else:
            self.copy("libzmq.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.name = "libzmq"
        # Ordered list of include paths
        self.cpp_info.includedirs = ['include']
        # The libs to link against
        self.cpp_info.libs = [
            "libzmq.so"] if self.options.shared else ["libzmq.a"]
        # Directories where libraries can be found
        self.cpp_info.libdirs = ['lib']
        # Directories where resources, data, etc can be found
        self.cpp_info.resdirs = []
        # Directories where executables and shared libs can be found
        self.cpp_info.bindirs = []
        # Directories where sources can be found (debugging, reusing sources)
        self.cpp_info.srcdirs = []
        self.cpp_info.build_modules = []  # Build system utility module files
        self.cpp_info.defines = []  # preprocessor definitions
        self.cpp_info.cflags = []  # pure C flags
        self.cpp_info.cxxflags = []  # C++ compilation flags
        self.cpp_info.sharedlinkflags = []  # linker flags
        self.cpp_info.exelinkflags = []  # linker flags
        self.cpp_info.system_libs = []  # The system libs to link against
