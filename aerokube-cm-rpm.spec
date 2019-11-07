%global _prefix /usr/local

Name:    aerokube-cm
Version: 1.7.1
Release: 1
Summary: Configuration manager for Aerokube products https://aerokube.com/cm/latest/
Group:   Development Tools
License: ASL 2.0
URL: https://github.com/aerokube/cm/releases/download/%{version}/cm_linux_amd64

%description
Configuration manager is used to automate installation of Aerokube products.

%prep
curl -L %{url} > cm_linux_amd64

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
cp cm_linux_amd64 %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

