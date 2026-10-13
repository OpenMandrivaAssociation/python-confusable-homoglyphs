%define module confusable-homoglyphs
%define oname confusable_homoglyphs

Name:		python-confusable-homoglyphs
Version:	3.3.1
Release:	2
Summary:	Detect confusable usage of unicode homoglyphs, prevent homograph attacks
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/confusable-homoglyphs/
# Upstream URL:	https://sr.ht/~valhalla/confusable_homoglyphs/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# For documentation
BuildRequires:	python%{pyver}dist(sphinx)
# Declare an explicit Require here as the module itself does not.
Requires:	python%{pyver}dist(click)

%description
Detect confusable usage of unicode homoglyphs, prevent homograph attacks.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%build -a
# Generate html docs
PYTHONPATH=${PWD} sphinx-build docs html
# Remove unrequired sphinx-build artifacts
rm -rf html/.{doctrees,buildinfo}

%files
%doc README.rst
%doc html
%{_bindir}/%{oname}
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}-py%{pyver}.egg-info
