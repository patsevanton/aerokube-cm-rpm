%global _prefix /usr/local

Name:    aerokube-cm
Version: 1.5.7
Release: 1
Summary: Configuration manager for Aerokube products https://aerokube.com/cm/latest/
Group:   Development Tools
License: ASL 2.0
Source0: https://github.com/aerokube/cm/releases/download/%{version}/cm_linux_amd64

%description
Configuration manager is used to automate installation of Aerokube products.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

