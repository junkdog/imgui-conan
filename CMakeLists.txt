cmake_minimum_required(VERSION 3.3)


project(imgui VERSION 1.5.2)

### Build Options ### todo
option(IMGUI_BUILD_EXAMPLES "Build examples" OFF)

### - ###
set(sources
    imgui.cpp
    imgui_draw.cpp
    imgui_demo.cpp
)

set(headers
    imgui.h
    stb_rect_pack.h
    stb_textedit.h 
    stb_truetype.h 
    imgui_internal.h

    imconfig.h
)

### properties ###
# auto-generated files
set(generated_dir "${CMAKE_CURRENT_BINARY_DIR}/generated")
set(version_config "${generated_dir}/${PROJECT_NAME}-config-version.cmake")
set(project_config "${generated_dir}/${PROJECT_NAME}-config.cmake")

# config
set(targets_export_name "${PROJECT_NAME}Targets")
set(namespace "${PROJECT_NAME}::")
set(desc_name ${PROJECT_NAME}-${PROJECT_VERSION})

# install directories
set(config_install_dir "lib/cmake/${PROJECT_NAME}")
set(include_install_dir "include")
set(root_lib_dir "lib")
set(lib_install_dir "${root_lib_dir}")


add_library(imgui
    ${sources}
    ${headers})

### Generate imgui_export.h
include(GenerateExportHeader)
generate_export_header(imgui)

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    "${version_config}" COMPATIBILITY SameMajorVersion
)

configure_package_config_file(
    "cmake/Config.cmake.in"
    "${project_config}"
    INSTALL_DESTINATION "${config_install_dir}"
)


### installing
# targets
install(
    TARGETS imgui
    EXPORT "${targets_export_name}"
    LIBRARY DESTINATION "${lib_install_dir}"
    ARCHIVE DESTINATION "${lib_install_dir}"
    RUNTIME DESTINATION "bin"
    INCLUDES DESTINATION "${include_install_dir}"
)

# headers
install(
    FILES ${headers}
    DESTINATION "${include_install_dir}/${PROJECT_NAME}"
)

# export headers
install(
    FILES "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}_export.h"
    DESTINATION "${include_install_dir}"
)

# imgui cmake files
install(
    FILES "${project_config}" "${version_config}"
    DESTINATION "${config_install_dir}"
)

# imguiTargets.cmake
install(
    EXPORT "${targets_export_name}"
    NAMESPACE "${namespace}"
    DESTINATION "${config_install_dir}"
)