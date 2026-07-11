%global tl_name href-ul
%global tl_revision 79622

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.3
Release:	%{tl_revision}.1
Summary:	Underscored LaTeX hyperlinks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/href-ul
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/href-ul.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/href-ul.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/href-ul.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyperref)
Requires:	texlive(ulem)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package makes hyperlinks underscored, just like on the web.
The package uses hyperref and ulem.

