<!-- [![Download](https://api.bintray.com/packages/conan-community/conan/opencv%3Aconan/images/download.svg) ](https://bintray.com/conan-community/conan/opencv%3Aconan/_latestVersion)
[![Build Status Travis](https://travis-ci.org/conan-community/conan-opencv.svg)](https://travis-ci.org/conan-community/conan-opencv)
[![Build Status AppVeyor](https://ci.appveyor.com/api/projects/status/github/conan-community/conan-opencv?svg=true)](https://ci.appveyor.com/project/ConanCIintegration/conan-opencv) -->

# Conan package recipe for [*libzmq*](https://github.com/zeromq/libzmq/)

The ZeroMQ lightweight messaging kernel is a library which extends the standard socket interfaces with features traditionally provided by specialised messaging middleware products. ZeroMQ sockets provide an abstraction of asynchronous message queues, multiple messaging patterns, message filtering (subscriptions), seamless access to multiple transport protocols and more.

<!-- # The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/conan-community/conan/opencv%3Aconan) -->

<!-- ## Issues

If you wish to report an issue or make a request for a package, please do so here:

[Issues Tracker](https://github.com/conan-community/community/issues) &rarr; aks for support and access -->

## For Users

### Basic setup

```bash
$ conan install libzmq/4.3.2@conan/stable
```

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

```bash
[requires]
libzmq/4.3.2@conan/stable

[generators]
cmake
```

Complete the installation of requirements for your project running:

```bash
$ mkdir build && cd build && conan install ..
```

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

```bash
$ conan create . conan/stable
```

### Available Options

| Option    | Default | Possible Values | Description                    |
| --------- | :------ | :-------------: | ------------------------------ |
| shared    | True    |  [True, False]  | Build shared libraries only    |
| fPIC      | True    |  [True, False]  | Set -fPIC compiler flag        |
| lobsodium | False   |  [True, False]  | Compile with libsodium support |

## Add Remote

Conan Community has its own Bintray repository, however, we are working to distribute all package in the Conan Center:

```bash
$ conan remote add conan-center "https://conan.bintray.com"
```

## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package libzmq.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](LICENSE)
