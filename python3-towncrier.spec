#
# Conditional build:
%bcond_with	tests	# Twisted tests

%define		module	towncrier
Summary:	Building newsfiles for your project
Summary(pl.UTF-8):	Tworzenie plików z nowościami dla własnego projektu
Name:		python3-%{module}
Version:	21.9.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/towncrier/
Source0:	https://files.pythonhosted.org/packages/source/t/towncrier/%{module}-%{version}.tar.gz
# Source0-md5:	9a6ba4f7d8e1c791fad29f3b276cad3d
# temporary, until we have tomli packaged
Patch0:		%{name}-no-tomli.patch
URL:		https://pypi.org/project/towncrier/
BuildRequires:	python3-incremental >= 17.5.0
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools >= 1:44.1.1
%if %{with tests}
BuildRequires:	python3-click
BuildRequires:	python3-click-default-group
BuildRequires:	python3-jinja2
BuildRequires:	python3-toml
BuildRequires:	python3-twisted
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
towncrier is a utility to produce useful, summarised news files for
your project. Rather than reading the Git history as some newer tools
to produce it, or having one single file which developers all write
to, towncrier reads "news fragments" which contain information useful
to end users.

%description -l pl.UTF-8
towncrier to narzędzie tworzące przydatne, podsumowujące pliki z listą
nowości dla danego projektu. Zamiasst czytania historii Gita, jak
robią niektóre nowsze narzędzia, albo nakazywania wszystkim
programistom pisania do jednego wspólnego pliku, towncrier czyta
"fragmenty nowości", zawierające informacje przydatne dla użytkowników
końcowych.

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%{__sed} -i -e 's/^import mock/from unittest import mock/' src/towncrier/test/test_create.py

%build
%py3_build

%if %{with tests}
trial-3 src/towncrier/test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/towncrier/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/towncrier
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}/templates
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
