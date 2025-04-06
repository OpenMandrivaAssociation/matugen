%global debug_package %{nil}

Name:		matugen
Version:	2.4.1
Release:	1
Source0:	https://github.com/InioX/matugen/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	A material you color generation tool
URL:		https://github.com/InioX/matugen
License:	GPL-2.0
Group:		Window Manager/Utility
BuildRequires:	cargo

%description
A material you color generation tool

%prep
%autosetup -p1
tar -zxf %{SOURCE1}
mkdir -p .cargo
cat >> .cargo/config.toml << EOF

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --release --frozen

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}
