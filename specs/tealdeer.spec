%bcond check 1
%global crate tealdeer
 
Name:           rust-tealdeer
Version:        1.7.1
Release:        %autorelease
Summary:        Fetch and show tldr help pages for many CLI commands
 
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tealdeer
Source:         %{crates_source}

Patch:          tealdeer-fix-metadata.diff
 
BuildRequires:  cargo-rpm-macros >= 24
 
%global _description %{expand:
Fetch and show tldr help pages for many CLI commands. Full featured
offline client with caching support.}
 
%description %{_description}
 
%package     -n %{crate}
Summary:        %{summary}
License:        Apache-2.0 AND MIT AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)

%description -n %{crate} %{_description}
 
%files       -n %{crate}
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE.dependencies
%doc README.md
%{_bindir}/tldr
%{bash_completions_dir}/tldr.bash
%{fish_completions_dir}/tldr.fish
%{zsh_completions_dir}/_tldr
 
%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
%generate_buildrequires
%cargo_generate_buildrequires
%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
 
%install
%cargo_install
install -Dpm0644 completion/bash_tealdeer %{buildroot}/%{bash_completions_dir}/tldr.bash
install -Dpm0644 completion/fish_tealdeer %{buildroot}/%{fish_completions_dir}/tldr.fish
install -Dpm0644 completion/zsh_tealdeer %{buildroot}/%{zsh_completions_dir}/_tldr
 
%if %{with check}
%check
%cargo_test -- --bins
%endif
 
%changelog
%autochangelog
