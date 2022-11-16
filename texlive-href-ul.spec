Name:		texlive-href-ul
Version:	64880
Release:	1
Summary:	Underscored LaTeX hyperlinks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/href-ul
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/href-ul.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/href-ul.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/href-ul.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package makes hyperlinks underscored, just like on
the web. The package uses hyperref and ulem.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/href-ul
%{_texmfdistdir}/tex/latex/href-ul
%doc %{_texmfdistdir}/doc/latex/href-ul

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
