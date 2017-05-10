%define modname nbnsd
%define appname %{modname}

Name:		%{appname}
Summary:	A minimal NetBIOS Name Service responder
Version:	0.1.0
Release:	1
License:	MIT
URL:		http://www.mostang.com/~davidm/nbnsd/
Source0:	%{modname}.tar.xz
Vendor:		PROCENTEC


%description
Windows-based machines can translate hostnames to IP addresses using a fairly simple protocol that is part of the NetBIOS on TCP/UDP specification (see RFCs 1001 and 1002). Samba supports such name-lookups via nmbd, but that program is big and complicated (about 1.6MiB compiled for ARM). If you just need to support the broadcast-based lookup service, that's overkill. To my surprise, I couldn't find a stand-alone, minimal daemon that would support just lookups (if I can't find it on Google in 5 minutes, does it really exist?), so I wrote one myself. I suspect there must be other such implementations out there. If you are aware of one, please let me know. Otherwise, feel free to use the code below, which is being distributed under the MIT license. Enjoy!

%global debug_package %{nil}

%prep
#unzip and move folder
%setup -q -c -n %{modname}


%build
%make_build %{?_smp_mflags}


%install
%make_install

%define servicefolder /etc/systemd/system
%{__install} -d $RPM_BUILD_ROOT%{servicefolder}
%{__cp} -r $RPM_BUILD_DIR/%{modname}/*.service $RPM_BUILD_ROOT%{servicefolder}


%files 
%{servicefolder}
%{_bindir}/nbnsd

%clean
rm -rf %{buildroot}

%changelog
* Fri May 5 2017 Sander Vermin <svermin@procentec.com> - 0.1.0
- Initial spec file
