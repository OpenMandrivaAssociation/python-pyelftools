%define module  pyelftools

Name:           python-%{module}
Version:        0.25
Release:        %mkrel 2
Summary:        Pure-python library for parsing ELF and DWARF
Group:          Development/Python
License:        Public Domain
URL:            https://github.com/eliben/pyelftools
Source0:        https://github.com/eliben/pyelftools/archive/v%{version}/%{module}-%{version}.tar.gz
BuildArch:      noarch

%description
pyelftools is a pure-Python library for parsing and analyzing ELF files
and DWARF debugging information.

%package -n     python2-%{module}
Summary:        Pure-python library for parsing ELF and DWARF for Python 2
Group:          Development/Python
BuildRequires:  python2-setuptools
BuildRequires:  python2-pkg-resources

%description -n python2-%{module}
pyelftools is a pure-Python library for parsing and analyzing ELF files
and DWARF debugging information.

This is the Python 2 module of pyelftools.

%package -n     python3-%{module}
Summary:        Pure-python library for parsing ELF and DWARF for Python 3
Group:          Development/Python
BuildRequires:  python3-setuptools
BuildRequires:  python-pkg-resources

%description -n python3-%{module}
pyelftools is a pure-Python library for parsing and analyzing ELF files
and DWARF debugging information.

This is the Python 3 module of pyelftools.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n       python2-%{module}
%doc CHANGES README.rst
%license LICENSE
%{python2_sitelib}/elftools/
%{python2_sitelib}/%{module}-%{version}-py%{python2_version}.egg-info

%files -n       python3-%{module}
%doc CHANGES README.rst
%license LICENSE
%{_bindir}/readelf.py
%{python3_sitelib}/elftools/
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info
