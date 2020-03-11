
"""
(c) 2019 Network To Code

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from network_importer.model import NetworkImporterSite



def test_site_import_prefix_from_ip():

    site = NetworkImporterSite(name="test")

    assert site.prefixes == {}

    site.add_prefix_from_ip("10.10.10.4/24")

    assert "10.10.10.0/24" in site.prefixes.keys()
    assert len(site.prefixes.keys()) == 1
    assert site.prefixes["10.10.10.0/24"].exist_local()

    site.add_prefix_from_ip("10.10.10.4/24")
    assert "10.10.10.0/24" in site.prefixes.keys()
    assert len(site.prefixes.keys()) == 1

    site.add_prefix_from_ip("12.12.10.4/32")
    assert "12.12.10.4/32" not in site.prefixes.keys()
    assert len(site.prefixes.keys()) == 1
