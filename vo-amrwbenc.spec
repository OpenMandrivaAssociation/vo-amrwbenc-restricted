%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		vo-amrwbenc
Version:	0.1.3
Release:	1
Summary:	VisualOn AMR-WB encoder library
License:	ASL 2.0
Group:		System/Libraries
URL:		https://opencore-amr.sourceforge.net/
Source0:	https://sourceforge.net/projects/opencore-amr/files/%{name}/%{name}-%{version}.tar.gz

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
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install


%files -n %{libname}
%doc COPYING ChangeLog NOTICE README
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
