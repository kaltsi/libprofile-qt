# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       libprofile-qt

# >> macros
# << macros

Summary:    Qt library for profiles
Version:    0.34.0.4
Release:    1
Group:      System/System Control
License:    LGPLv2.1
URL:        http://github.com/nemomobile/libprofile-qt
Source0:    %{name}-%{version}.tar.bz2
Source100:  libprofile-qt.yaml
Requires:   profiled
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  doxygen

%description
Qt wrapper library for profiles

%package -n libprofile-qt-devel
Summary:    Development headers for libprofile-qt library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig(QtCore)
Requires:   libprofile-qt = %{version}

%description -n libprofile-qt-devel
Development headers for libprofile-qt library


%package -n libprofile-qt-tests
Summary:    Unit tests for libprofile-qt
Group:      Development/System
Requires:   %{name} = %{version}-%{release}
Requires:   libprofile-qt = %{version}

%description -n libprofile-qt-tests
Unit tests for libprofile-qt


%package -n libprofile-qt-doc
Summary:    API documentation for libprofile-qt
Group:      Documentation
BuildArch:    noarch
Requires:   %{name} = %{version}-%{release}

%description -n libprofile-qt-doc
API documentation for libprofile-qt



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libprofile-qt.so.*
# >> files
# << files

%files -n libprofile-qt-devel
%defattr(-,root,root,-)
%{_libdir}/libprofile-qt.so
%{_includedir}/profile-qt/Profile
%{_includedir}/profile-qt/profile.h
# >> files libprofile-qt-devel
# << files libprofile-qt-devel

%files -n libprofile-qt-tests
%defattr(-,root,root,-)
%{_libdir}/libprofile-qt-tests/ut_profile
%{_datadir}/libprofile-qt-tests/tests.xml
# >> files libprofile-qt-tests
# << files libprofile-qt-tests

%files -n libprofile-qt-doc
%defattr(-,root,root,-)
%{_docdir}/libprofile-qt/*
# >> files libprofile-qt-doc
# << files libprofile-qt-doc
