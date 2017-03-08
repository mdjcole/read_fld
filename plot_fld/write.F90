PROGRAM write
!Tool to produce example [un]formatted fortran output files
  IMPLICIT NONE

    INTEGER :: nunit = 1
    INTEGER :: i=1
    INTEGER :: j, k
    REAL, DIMENSION(5) :: header
    INTEGER, DIMENSION(1000) :: dat
    DOUBLE PRECISION, DIMENSION(16,100) :: fftdat

    DO WHILE (i < 6)
      header(i) = i*2.
      i=i+1
    END DO

    i=1
    DO WHILE (i < 1001)
      dat(i) = i*5
      i=i+1
    END DO

    fftdat(:,:)=0.0
    DO k=1,100
      fftdat(7,k)=SIN(k*3.142/100)
    END DO

!    DO j = 1, 100
!      DO k = 1, 16
!        fftdat(k,j)=k+(j-1)*16
!        PRINT*,fftdat(k,j)
!      END DO
!    END DO

    OPEN(UNIT=nunit, STATUS='new', FILE='test.dat',&
       POSITION='rewind', ACTION='write', FORM='unformatted')
!   OPEN(UNIT=nunit, STATUS='new', FILE='test.dat',&
!      POSITION='rewind', ACTION='write', FORM='formatted')

!    WRITE(UNIT=nunit) header(:)
!    WRITE(UNIT=nunit) dat(:)
!    WRITE(UNIT=nunit,FMT=*) dat(:)
    WRITE(UNIT=nunit) fftdat(:,:)

    CLOSE(UNIT=nunit)

END PROGRAM
