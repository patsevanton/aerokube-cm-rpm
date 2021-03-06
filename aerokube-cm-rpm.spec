%global _prefix /usr/local

Name:    aerokube-cm
Version: 1.7.2
Release: 1
Summary: Configuration manager for Aerokube products https://aerokube.com/cm/latest/
Group:   Development Tools
License: ASL 2.0
Source0: build.sh
URL: https://github.com/aerokube/cm/releases/download/%{version}/cm_linux_amd64

%description
Configuration manager is used to automate installation of Aerokube products.

%prep
echo "curl -L %{url} > cm_linux_amd64"
curl -L %{url} > cm_linux_amd64

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
install -p -m 0755 cm_linux_amd64 %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
