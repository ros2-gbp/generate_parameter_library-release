%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-generate-parameter-library
Version:        0.3.8
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS generate_parameter_library package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       fmt-devel
Requires:       ros-iron-generate-parameter-library-py
Requires:       ros-iron-parameter-traits
Requires:       ros-iron-rclcpp
Requires:       ros-iron-rclcpp-lifecycle
Requires:       ros-iron-rclpy
Requires:       ros-iron-rsl
Requires:       ros-iron-tcb-span
Requires:       ros-iron-tl-expected
Requires:       ros-iron-ros-workspace
BuildRequires:  fmt-devel
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-ament-cmake-python
BuildRequires:  ros-iron-parameter-traits
BuildRequires:  ros-iron-rclcpp
BuildRequires:  ros-iron-rclcpp-lifecycle
BuildRequires:  ros-iron-rclpy
BuildRequires:  ros-iron-rsl
BuildRequires:  ros-iron-tcb-span
BuildRequires:  ros-iron-tl-expected
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-lint-auto
BuildRequires:  ros-iron-ament-lint-common
%endif

%description
CMake to generate ROS parameter library.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Wed Apr 03 2024 Paul Gesel <paul.gesel@picknik.ai> - 0.3.8-2
- Autogenerated by Bloom

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

