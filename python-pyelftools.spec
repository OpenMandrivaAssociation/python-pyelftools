%define module pyelftools

Name:		python-%{module}
Version:	0.29
Release:	2
Summary:	Pure-python library for parsing ELF and DWARF
Group:		Development/Python
License:	Public Domain
URL:		https://github.com/eliben/pyelftools
Source0:	https://github.com/eliben/pyelftools/archive/v%{version}/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  python3-setuptools
BuildRequires:  python-pkg-resources
%rename		python-elftools
Obsoletes:	python2-pyelftools < 0.29-2

%description
pyelftools is a pure-Python library for parsing and analyzing ELF files
and DWARF debugging information.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc CHANGES README.rst
%license LICENSE
%{_bindir}/readelf.py
%{python3_sitelib}/elftools/
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info
