%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-generate-parameter-library-py
Version:        0.3.8
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS generate_parameter_library_py package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-yaml
Requires:       python3-jinja2
Requires:       python3-typeguard
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-yaml
BuildRequires:  python3-jinja2
BuildRequires:  python3-typeguard
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-iron-ament-copyright
%endif

%description
Python to generate ROS parameter library.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Fri Mar 08 2024 Paul Gesel <paul.gesel@picknik.ai> - 0.3.8-1
- Autogenerated by Bloom

* Fri Jan 12 2024 Paul Gesel <paul.gesel@picknik.ai> - 0.3.7-1
- Autogenerated by Bloom

* Mon Jul 31 2023 Paul Gesel <paul.gesel@picknik.ai> - 0.3.6-1
- Autogenerated by Bloom

* Fri Jul 28 2023 Paul Gesel <paul.gesel@picknik.ai> - 0.3.5-1
- Autogenerated by Bloom

* Mon Jul 24 2023 Paul Gesel <paul.gesel@picknik.ai> - 0.3.4-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Paul Gesel <paul.gesel@picknik.ai> - 0.3.3-2
- Autogenerated by Bloom

* Thu Apr 13 2023 Paul Gesel <paul.gesel@picknik.ai> - 0.3.3-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Paul Gesel <paul.gesel@picknik.ai> - 0.3.2-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Paul Gesel <paul.gesel@picknik.ai> - 0.3.1-3
- Autogenerated by Bloom

