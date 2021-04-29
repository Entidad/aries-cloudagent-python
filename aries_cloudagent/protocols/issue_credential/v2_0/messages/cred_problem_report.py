"""A problem report message."""

from marshmallow import EXCLUDE

from ....problem_report.v1_0.message import ProblemReport, ProblemReportSchema

from ..message_types import CRED_20_PROBLEM_REPORT, PROTOCOL_PACKAGE

HANDLER_CLASS = (
    f"{PROTOCOL_PACKAGE}.handlers.problem_report_handler.ProblemReportHandler"
)


class V20CredProblemReport(ProblemReport):
    """Class representing a problem report message."""

    class Meta:
        """Problem report metadata."""

        handler_class = HANDLER_CLASS
        schema_class = "V20CredProblemReportSchema"
        message_type = CRED_20_PROBLEM_REPORT

    def __init__(self, **kwargs):
        """Initialize problem report object."""
        super().__init__(**kwargs)


class V20CredProblemReportSchema(ProblemReportSchema):
    """Problem report schema."""

    class Meta:
        """Schema metadata."""

        model_class = V20CredProblemReport
        unknown = EXCLUDE
