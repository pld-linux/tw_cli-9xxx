%define	model	9550sx
Summary:	Utility to control 3ware SATA RAID controllers
Summary(pl.UTF-8):	Narzędzie do sterowania kontrolerami SATA RAID firmy 3ware
Name:		tw_cli-%{model}
Version:	9.3.0.7
Release:	1
License:	commercial
Group:		Base
Source0:	http://www.3ware.com/download/Escalade9550SX-Series/9.3.0.7/tw_cli-linux-x86_64-%{version}.tgz
Source1:	http://www.3ware.com/download/Escalade9550SX-Series/9.3.0.7/tw_cli-linux-x86-%{version}.tgz
URL:		http://www.3ware.com/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to control 3ware SATA RAID controllers.

%description -l pl.UTF-8
Narzędzie do sterowania kontrolerami SATA RAID firmy 3ware.

%prep
%setup -q -c -T
%ifarch %{ix86}
tar xf %{SOURCE1}
%endif
%ifarch %{x8664}
tar xf %{SOURCE0}
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install tw_cli $RPM_BUILD_ROOT%{_sbindir}/tw_cli-%{model}
install tw_sched $RPM_BUILD_ROOT%{_sbindir}/tw_sched-%{model}

install tw_cli.8.nroff $RPM_BUILD_ROOT%{_mandir}/man8/tw_cli-%{model}.8
install tw_sched.8.nroff  $RPM_BUILD_ROOT%{_mandir}/man8/tw_sched-%{model}.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc tw_sched.cfg
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
