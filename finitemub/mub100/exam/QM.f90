program QM

  implicit none

  real(8) pi,hc
  parameter(pi=3.141592653589793d0)
  parameter(hc=197.33)
  real(8) T,mu !temperature and chemical potential
  real(8) l,lb !polyakov loop
  real(8) rho0,mPion,mSigma,mf,Vtotal,fpi,h,Zphi,Zpsi,c,kappa
  real(8) sigma_UV,kappa_UV_i,kappa_UV_i_mu,kappa_UV
  real(8) Vtotal0
  real(8) Ti,dT,mu_down,mu_up,mudelta
  integer i,iTmax,j,jmumax,m,mm,i_mm,j1
  parameter(iTmax=300,jmumax=51)
  real(8) pre_res(0:jmumax,0:iTmax),T_res(0:iTmax),mu_res(0:jmumax,0:iTmax),pre_com(jmumax)
  real(8) mu_bound(0:iTmax),mu_bound_low,mu_bound_high
  real(8) T_MeV,muB_MeV
  real(8) mui,muBi,muB
  integer mmax
  parameter(mmax=10)
!order of chebyshev polynomial
  real(8) dcd0mu(mmax),dcd1mu(mmax),dcd2mu(mmax),dcd3mu(mmax),dcd4mu(mmax),chi(mmax,0:iTmax)
  real(8) factorial
  real(8) fpi_res(0:jmumax,0:iTmax),mPion_res(0:jmumax,0:iTmax),mSigma_res(0:jmumax,0:iTmax),mf_res(0:jmumax,0:iTmax)
  integer iT,iv
  real(8) l_i,lb_i,l_i_mu,lb_i_mu
  real(8) Fnf0,Fnf1,Fnf2
  external Fnf0,Fnf1,Fnf2
  real(8) nfl,nfl0,nfl1,lset
  real(8) chebev
  external chebev


  common /Tmu/ T,mu
  common /prefit/ pre_com
  common /iTiv/ iT,iv

  dT=1.

  muBi=100./hc

  open(unit=11,file='m1.dat')
  read(11,*) j1
  close (11)
  write(*,*)'load OK',j1
  
  j=j1

  sigma_UV=100./hc
  kappa_UV_i=sigma_UV**2/2.

  l_i=1.e-10
  lb_i=1.e-10

  mu_up=250./hc
  mu_down=-mu_up

  mudelta=cos(pi*(j-0.5Q+00)/real(jmumax,kind=16))*(0.5Q+00*(mu_up-mu_down))+0.5Q+00*(mu_up+mu_down)

  do i=1,iTmax
    T_MeV=dT*real(i,kind=16)
    T=T_MeV/hc

    muB=muBi+mudelta
    mu=muB/3.Q+0
    muB_MeV=muB*hc

      call selfEQ(kappa_UV_i,l_i,lb_i,kappa_UV,l,lb,rho0,mPion,mSigma,mf,Vtotal,fpi,h,Zphi,Zpsi,c,kappa)
      kappa_UV_i=kappa_UV
      l_i=l
      lb_i=lb

    write(*,"('i=', I4)")i
    write(*,"('muB_MeV=', f15.7, t25, 'T_MeV=', f15.7)")muB_MeV,T_MeV
    !write(*,"('fpi=', f15.7, t25, 'mPion=', f15.7)")fpi*hc,mPion*hc
    !write(*,"('kappa_UV=', e21.14)")kappa_UV

    open(unit=51,file='./buffer/TMeV.dat',position='append')
    write(51,*)T_MeV
    close(51)

    open(unit=51,file='./buffer/mPion.dat',position='append')
    write(51, "(e21.14)")mPion*hc
    close(51)

    open(unit=51,file='./buffer/mSigma.dat',position='append')
    write(51,*)mSigma*hc
    close(51)

    open(unit=51,file='./buffer/mf.dat',position='append')
    write(51,*)mf*hc
    close(51)

    open(unit=51,file='./buffer/Vtotal.dat',position='append')
    write(51,*)Vtotal
    close(51)

    open(unit=51,file='./buffer/fpi.dat',position='append')
    write(51,*)fpi*hc
    close(51)


  end do



end






