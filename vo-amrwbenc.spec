%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		vo-amrwbenc
Version:	0.1.2
Release:	%mkrel 1
Summary:	VisualOn AMR-WB encoder library
License:	ASL 2.0
Group:		System/Libraries
URL:		http://opencore-amr.sourceforge.net/
Source0:	http://sourceforge.net/projects/opencore-amr/files/%{name}/%{name}-%{version}.tar.gz

%description
This library contains an encoder implementation of the Adaptive Multi
Rate Wideband (AMR-WB) audio codec. The library is based on a codec
implementation by VisualOn as part of the Stagefright framework from
the Google Android project.

This package is in restricted because the AMR audio compression scheme 
is covered by patents.

%package -n %{libname}
Group:		System/Libraries
Summary:	VisualOn AMR-WB encoder library

%description -n %{libname}
This library contains an encoder implementation of the Adaptive Multi
Rate Wideband (AMR-WB) audio codec. The library is based on a codec
implementation by VisualOn as part of the Stagefright framework from
the Google Android project.

This package is in restricted because the AMR audio compression scheme 
is covered by patents.

%package -n %{develname}
Group:		Development/C
Summary:	development files for %{name} AMR wideband encoding library
Provides:	libvo-amrwbenc-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Header files and development libraries for %{name}

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__rm -f %{buildroot}%{_libdir}/*.la

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog NOTICE README
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu May 17 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.1.2-1
- New version 1.2
- Add docs
- Change tainted to restricted in description

* Sun Feb 05 2012 fwang <fwang> 0.1.1-3.mga2
+ Revision: 205065
- drop .la file

* Thu May 26 2011 cjw <cjw> 0.1.1-2.mga1.tainted
+ Revision: 100422
- add missing library dependency on devel package

* Mon May 09 2011 cjw <cjw> 0.1.1-1.mga1
+ Revision: 96780
- add 'tainted' notice
- imported package vo-amrwbenc

