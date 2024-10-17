Name:		texlive-context-cmscbf
Version:	47085
Release:	2
Summary:	Use Computer Modern bold Caps and Small-caps in ConTeXt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/context-cmscbf
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-cmscbf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-cmscbf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The module makes provision for bold caps and small caps CM
fonts, in ConTeXt. Such a font may be found in the Computer
Modern 'extra bold' font set.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/context/third/cmscbf
%doc %{_texmfdistdir}/doc/context/third/cmscbf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
