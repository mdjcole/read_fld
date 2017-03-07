PROGRAM bmax_calc
!Tool to convert unformatted (binary) angy_phi_pol.fld file to formatted (human readable)
  IMPLICIT NONE

    INTEGER :: nunit = 1
    INTEGER :: i=1
    REAL, DIMENSION(5) :: header
    INTEGER, DIMENSION(1000) :: dat

    DO WHILE (i < 6)
      header(i) = i*2.
      i=i+1
    END DO

    i=1
    DO WHILE (i < 1001)
      dat(i) = i*5
      i=i+1
    END DO

    OPEN(UNIT=nunit, STATUS='new', FILE='test.dat',&
       POSITION='rewind', ACTION='write', FORM='unformatted')
!    OPEN(UNIT=nunit, STATUS='new', FILE='test.dat',&
!       POSITION='rewind', ACTION='write', FORM='formatted')

!    WRITE(UNIT=nunit) header(:)
    WRITE(UNIT=nunit) dat(:)
!    WRITE(UNIT=nunit,FMT=*) dat(:)

    CLOSE(UNIT=nunit)

END PROGRAM
