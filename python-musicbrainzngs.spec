#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 bindings for the MusicBrainz NGS and the Cover Art Archive webservices
Name:		python-musicbrainzngs
Version:	0.6
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/musicbrainzngs
Source0:	https://pypi.python.org/packages/63/cc/67ad422295750e2b9ee57c27370dc85d5b85af2454afe7077df6b93d5938/musicbrainzngs-%{version}.tar.gz
# Source0-md5:	22616f1710f13a8da933920089c51441
URL:		https://python-musicbrainzngs.readthedocs.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library implements webservice bindings for the Musicbrainz NGS
site, also known as /ws/2 and the Cover Art Archive.

%package -n python3-musicbrainzngs
Summary:	Python 3 bindings for the MusicBrainz NGS and the Cover Art Archive webservices
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-musicbrainzngs
This library implements webservice bindings for the Musicbrainz NGS 
site, also known as /ws/2 and the Cover Art Archive.

%prep
%setup -q -n musicbrainzngs-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README.rst
%{py_sitescriptdir}/musicbrainzngs
%{py_sitescriptdir}/musicbrainzngs-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-musicbrainzngs
%defattr(644,root,root,755)
%doc CHANGES COPYING README.rst
%{py3_sitescriptdir}/musicbrainzngs
%{py3_sitescriptdir}/musicbrainzngs-%{version}-py*.egg-info
%endif
