%global _prefix /usr/local

Name:    aerokube-cm
Version: 1.7.1
Release: 2
Summary: Configuration manager for Aerokube products https://aerokube.com/cm/latest/
Group:   Development Tools
License: ASL 2.0
URL: https://github.com/aerokube/cm/releases/download/%{version}/cm_linux_amd64

%description
Configuration manager is used to automate installation of Aerokube products.

%prep
echo "curl -L %{url} > cm_linux_amd64"
curl -L %{url} > cm_linux_amd64
ls
pwd

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
install -p -m 0755 cm_linux_amd64 %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
