%define debug_package %{nil}

Name:		model-config-tm1
Summary:	A Model configuration
Version:	0.0.1
Release:	0
Group:		System/Configuration
License:	Apache-2.0
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz

%description
Model configuration data package

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/config
cp -f model-config.xml %{buildroot}%{_sysconfdir}/config/model-config.xml

%files
%{_sysconfdir}/config/model-config.xml
%manifest model-config.manifest
