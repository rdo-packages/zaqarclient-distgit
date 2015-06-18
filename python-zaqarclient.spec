Name:           python-zaqarclient
Version:        0.1.0
Release:        4%{?dist}
Summary:        Client Library for OpenStack Zaqar Queueing API

License:        ASL 2.0
URL:            http://wiki.openstack.org/zaqar
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires:       python-jsonschema
Requires:       python-keystoneclient
Requires:       python-pbr
Requires:       python-six
Requires:       python-stevedore

%description
Python client to Zaqar messaging service API v1

%prep
%setup -q

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst ChangeLog examples
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{python2_sitelib}/zaqarclient
%{python2_sitelib}/python_zaqarclient-%{version}-py?.?.egg-info

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.0-3
- Drop PBR patch

* Mon Sep 29 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.0-2
- Drop PBR runtime dependency

* Sun Sep 28 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.0-1
- Initial package.
