%define		module	towncrier
Summary:	Building newsfiles for your project
Name:		python3-%{module}
Version:	21.3.0
Release:	0.1
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/t/towncrier/%{module}-%{version}.tar.gz
# Source0-md5:	ae3ba211d45e80731b7a974aa1d6ffd2
URL:		https://pypi.org/project/towncrier/
BuildRequires:	python3-incremental
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
towncrier is a utility to produce useful, summarised news files for
your project. Rather than reading the Git history as some newer tools
to produce it, or having one single file which developers all write
to, towncrier reads “news fragments” which contain information useful
to end users.

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

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/towncrier/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.rst NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/towncrier
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}/templates
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
