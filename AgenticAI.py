import csv
from datetime import datetime

# ==============================
# Autonomous Security Agent
# ==============================

class SecurityAgent:
    def __init__(self):
        self.blocked_flows = []
        self.monitoring_level = "NORMAL"

    def take_action(self, prediction, flow_id=None):

        if prediction == "Attack":
            decision = "Threat Confirmed"
            actions = [
                "Alert Generated",
                "Logged",
               
                "IP Blocked"
            ]

            if flow_id is not None:
                self.blocked_flows.append(flow_id)

            self.monitoring_level = "HIGH"

        else:
            decision = "Safe Traffic"
            actions = ["Monitoring"]
            self.monitoring_level = "NORMAL"

        return decision, actions

    def get_status(self):
        return {
            "blocked_flows": self.blocked_flows,
            "monitoring_level": self.monitoring_level
        }


# Global agent instance
agent = SecurityAgent()