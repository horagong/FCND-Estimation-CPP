cmake_minimum_required(VERSION 3.9)
project(CPPSim)

set(CMAKE_CXX_STANDARD 11)
if (APPLE)
        set(__APPLE__ ${APPLE})
        message("${__APPLE__}")
endif(APPLE)

add_executable(CPPSim
#        ${SOURCES}
#        ${HEADERS}
        )
find_package(PkgConfig REQUIRED)
find_package(freeglut QUIET)
if (NOT freeglut_FOUND)
        pkg_check_modules(freeglut REQUIRED freeglut)
endif()
#find_package(Qt5Core REQUIRED)
#find_package(Qt5Network REQUIRED)
#find_package(Qt5Widgets REQUIRED)

find_package(OpenGL REQUIRED)
#find_package(GL REQUIRED)
#find_package(pthread REQUIRED)

file(GLOB SOURCES
        src/*.cpp
        src/Drawing/*.cpp
        src/Math/*.cpp
        src/Simulation/*.cpp
        src/Utility/*.cpp
        src/MavlinkNode/*.cpp
        src/MavlinkNode/*.h)
        
target_include_directories(CPPSim PUBLIC src lib)
target_sources(CPPSim PUBLIC ${SOURCES})
target_link_libraries(CPPSim
#        Qt5::Core
#        Qt5::Network
#        Qt5::Widgets
        ${freeglut_LIBRARIES}
        ${OPENGL_LIBRARIES}
#        GLU
#        GL
#        pthread
        )

#set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -std=c++0x")



#file(GLOB HEADERS
#        src/*.h
#        src/Drawing/*.h
#        src/Math/*.h
#        src/Simulation/*.h
#        src/Utility/*.h
#        lib/matrix/*.hpp
#        lib/mavlink/*.h
#        lib/mavlink/common/*.h)



