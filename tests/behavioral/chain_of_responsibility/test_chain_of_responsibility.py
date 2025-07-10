import sys
import unittest
from io import StringIO

from examples.behavioral.chain_of_responsibility.chain_of_responsibility import (
    Director,
    Manager,
    TeamLeader,
)


class TestLeaveApprovalChain(unittest.TestCase):
    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = self.captured_output = StringIO()

        self.team_leader = TeamLeader()
        self.manager = Manager()
        self.director = Director()
        self.team_leader.set_next(self.manager).set_next(self.director)

    def tearDown(self):
        sys.stdout = self._stdout

    def test_team_leader_approval(self):
        self.team_leader.handle(1)
        output = self.captured_output.getvalue()
        self.assertIn("TeamLeader: 批准 1 天请假", output)

    def test_manager_approval(self):
        self.team_leader.handle(3)
        output = self.captured_output.getvalue()
        self.assertIn("Manager: 批准 3 天以内请假", output)

    def test_director_approval(self):
        self.team_leader.handle(6)
        output = self.captured_output.getvalue()
        self.assertIn("Director: 批准 7 天以内请假", output)

    def test_request_too_long(self):
        self.team_leader.handle(10)
        output = self.captured_output.getvalue()
        self.assertIn("Director: 拒绝，请假太长", output)


# ====== 运行入口 ======
if __name__ == "__main__":
    unittest.main()
