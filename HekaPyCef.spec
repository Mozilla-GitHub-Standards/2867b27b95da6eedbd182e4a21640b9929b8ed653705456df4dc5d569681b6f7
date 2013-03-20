%define name heka-py-cef
%define pythonname HekaPyCef
%define version 0.2
%define unmangled_version %{version}
%define release 0

Summary: CEF plugin for heka
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{pythonname}-%{unmangled_version}.tar.gz
License: MPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Victor Ng <vng@mozilla.com>
Requires: 
Obsoletes:

Url: https://github.com/mozilla-services/heka-py-cef

%description
==================================
CEF data capture plugin for Heka
==================================

A plugin for 'Heka' which provides extensions to log CEF compatible
messages.

%prep
%setup -n %{pythonname}-%{unmangled_version} -n %{pythonname}-%{unmangled_version}

%build
python2.6 setup.py build

%install
python2.6 setup.py install --single-version-externally-managed --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES

%defattr(-,root,root)
