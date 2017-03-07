PROGRAM bmax_calc
!Tool to convert unformatted (binary) angy_phi_pol.fld file to formatted (human readable)
  IMPLICIT NONE

  CHARACTER(LEN=80) :: file_name = "prod_msdmp_angy_phi_pol.fld"

  CALL header_convert(file_name)

!  CALL body_convert(file_name)

  CONTAINS
  
  SUBROUTINE header_convert(file_name)
    !read binary header, create output file and write out human readable header

    CHARACTER(LEN=80), INTENT(IN) :: file_name
    CHARACTER(LEN=80) :: out_name
    INTEGER :: nunit = 1
    
    CHARACTER(LEN=80) :: codename_str    
    REAL :: VERNUM    
    REAL :: zverformat    
    INTEGER :: NUM_INT_HEADER    
    REAL, DIMENSION(34) :: int_header    
    INTEGER :: NUM_REAL_HEADER    
    REAL, DIMENSION(51) :: zreal_header    

    COMPLEX, DIMENSION(33, 128) :: cfftdata
    REAL :: simtime
    INTEGER :: mmin_filter, im_number
    
    OPEN(UNIT=nunit, STATUS='old', FILE=file_name,&
       POSITION='rewind', ACTION='read', FORM='unformatted')

    READ(UNIT=nunit) codename_str    
    READ(UNIT=nunit) VERNUM    
    READ(UNIT=nunit) zverformat    
    READ(UNIT=nunit) NUM_INT_HEADER
    READ(UNIT=nunit) int_header(:)
    READ(UNIT=nunit) NUM_REAL_HEADER
    READ(UNIT=nunit) zreal_header(:)      

    READ(UNIT=nunit) simtime, mmin_filter, im_number
    READ(UNIT=nunit) cfftdata

    CLOSE(UNIT=nunit)

    nunit=2
    out_name="FORMAT_OUT_" // file_name
    
    OPEN(UNIT=nunit, STATUS='new', FILE=out_name,&
         POSITION='rewind', ACTION='write', FORM='formatted')

    WRITE(UNIT=nunit,FMT=*) codename_str    
    WRITE(UNIT=nunit,FMT=*) VERNUM    
    WRITE(UNIT=nunit,FMT=*) zverformat    
    WRITE(UNIT=nunit,FMT=*) NUM_INT_HEADER    
    WRITE(UNIT=nunit,FMT=*) int_header(:)    
    WRITE(UNIT=nunit,FMT=*) NUM_REAL_HEADER    
    WRITE(UNIT=nunit,FMT=*) zreal_header(:)    

    WRITE(UNIT=nunit,FMT=*) simtime, mmin_filter, im_number
    WRITE(UNIT=nunit,FMT=*) cfftdata

    CLOSE(UNIT=nunit)

  END SUBROUTINE header_convert

  SUBROUTINE body_convert(file_name)

    INTEGER :: nunit = 1
    CHARACTER(LEN=80), INTENT(IN) :: file_name

    COMPLEX, DIMENSION(33, 128) :: cfftdata
    REAL :: simtime
    INTEGER :: mmin_filter, im_number

    OPEN(UNIT=nunit, STATUS='old', FILE=file_name,&
       POSITION='append', ACTION='read', FORM='unformatted')    

    READ(UNIT=nunit) simtime, mmin_filter, im_number
    READ(UNIT=nunit) cfftdata

    CLOSE(UNIT=1)   

  END SUBROUTINE body_convert

END PROGRAM
