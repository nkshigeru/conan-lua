import os
from conans import ConanFile, CMake, tools, VisualStudioBuildEnvironment


class LuaConan(ConanFile):
    name = "lua"
    version = "5.1.5"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Lua here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    source_subfolder = "lua-{version}".format(version=version)

    def source(self):
        url = "https://www.lua.org/ftp/lua-{version}.tar.gz".format(version=self.version)
        tools.get(url)

    def build(self):
        if self.settings.compiler == "Visual Studio":
            #TODO debug build
            with tools.chdir(self.source_subfolder):
                with tools.vcvars(self.settings):
                    self.run("etc\\luavs.bat")

    def package(self):
        src = os.path.join(self.source_subfolder, "src")
        etc = os.path.join(self.source_subfolder, "etc")
        self.copy("lua.h", dst="include", src=src, keep_path=False)
        self.copy("luaconf.h", dst="include", src=src, keep_path=False)
        self.copy("lualib.h", dst="include", src=src, keep_path=False)
        self.copy("lauxlib.h", dst="include", src=src, keep_path=False)
        self.copy("lua.hpp", dst="include", src=etc, keep_path=False)
        self.copy("lua51.lib", dst="lib", src=src, keep_path=False)
        self.copy("lua51.dll", dst="bin", src=src, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lua51"]

