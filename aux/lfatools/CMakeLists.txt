if(CMAKE_Fortran_COMPILER_ID MATCHES "GNU")
#    set(dialect "-std=legacy -ffree-form -fimplicit-none")
    set(dialect "-fconvert=big-endian -cpp")
    set(bounds "-fbounds-check")
endif()
if(CMAKE_Fortran_COMPILER_ID MATCHES "Intel")
    set(dialect "-convert big_endian -cpp")
    set(bounds "-check bounds")
endif()
set (CMAKE_Fortran_FLAGS_RELEASE "-O2")
set (CMAKE_Fortran_FLAGS_DEBUG   "-O0 -g")

set(CMAKE_Fortran_FLAGS_DEBUG "${CMAKE_Fortran_FLAGS_DEBUG} ${bounds}")
set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} ${dialect}")


set(HEADER_FILES lfatail.h lfayom.h)
add_library(lfa lfa.f90 ${HEADER_FILES})

add_executable(cllangu cllangu.f90)

set(LFAPROGS lfac lfafreq lfacre lfalaf lfaminm lfareu lfatest lfa_demo lfadiffart lfadiffrel lfadiff lfa2lfa lfamoy lfa_autodocumentation)
set(LFALFPPROGS lfa2lfp lfp2lfa)
set(EXECUTABLES ${LFAPROGS} ${LFALFPPROGS})

foreach (p ${LFAPROGS})
  add_executable (${p} "${p}.f90")
  target_link_libraries(${p} lfa)
endforeach (p)

foreach (p ${LFALFPPROGS})
  add_executable (${p} "${p}.f90" lfp.f90 ${HEADER_FILES})
  target_link_libraries(${p} lfa)
endforeach (p)

install (TARGETS ${EXECUTABLES}
         PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ GROUP_EXECUTE GROUP_READ
         RUNTIME DESTINATION "bin")

install (TARGETS lfa RUNTIME DESTINATION "lib")

