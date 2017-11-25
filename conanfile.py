from conans import ConanFile, CMake
from shutil import move

class ImguiConan(ConanFile):
    generators = "cmake"
    name = "imgui"
    version = "1.52"
    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "cmake/Config.cmake.in"

    def source(self):
        self.run("git clone https://github.com/ocornut/imgui.git")
        self.run("cd imgui && git checkout tags/v%s" % self.version)
        move("%s/CMakeLists.txt" % self.source_folder,
             "%s/imgui" % self.source_folder)
        move("%s/cmake" % self.source_folder,
             "%s/imgui/" % self.source_folder)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="%s/imgui" % self.source_folder)
        cmake.build(target="install")

    def package_info(self):
        self.cpp_info.libs = ["imgui"]
