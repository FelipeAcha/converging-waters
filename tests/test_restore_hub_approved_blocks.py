import unittest
from scripts.restore_hub_approved_blocks import restore, span_by_id, strip_authorized_baseline, strip_authorized_candidate


class HubRecoveryRegression(unittest.TestCase):
    def test_only_three_authorized_regions_change(self):
        baseline = '''<html><body><div id="keep-a">A</div><section id="stanley-update"><p>bad stanley</p></section><div id="keep-b">B</div><section id="alliance-architecture"><p>bad alliance</p></section><div id="keep-c">C</div><section id="current-session"><p>current</p></section><div id="keep-d">D</div></body></html>'''
        approved_early = '''<html><body><div id="principal-infographic"><figure><img src="assets/asset-be0fa6e11454.webp"></figure></div><section id="stanley-update">''' + ''.join('<a href="https://example.com"><img src="assets/x.webp"></a>' for _ in range(13)) + ''.join('<a href="https://example.com">x</a>' for _ in range(4)) + '''</section></body></html>'''
        approved_alliance = '''<html><body><section id="alliance-architecture"><h2>Approved alliance</h2><p>matrix restored</p></section></body></html>'''
        candidate, report = restore(baseline, approved_early, approved_alliance)
        self.assertEqual(strip_authorized_baseline(baseline), strip_authorized_candidate(candidate))
        self.assertIn('id="principal-infographic"', candidate)
        self.assertIn('assets/legacy/asset-be0fa6e11454.webp', candidate)
        self.assertEqual(span_by_id(candidate, 'stanley-update')[2].count('<img'), 13)
        self.assertEqual(span_by_id(candidate, 'stanley-update')[2].count('<a '), 17)
        self.assertIn('Approved alliance', span_by_id(candidate, 'alliance-architecture')[2])
        self.assertEqual(report['untouched_bytes'], 'EXACT_AFTER_REMOVING_3_AUTHORIZED_REGIONS')


if __name__ == '__main__':
    unittest.main()
