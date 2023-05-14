"""change db

Revision ID: 788438e53731
Revises: 8894e39184ff
Create Date: 2023-05-14 21:38:32.547047

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "788438e53731"
down_revision = "8894e39184ff"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("availability_schedule", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("availability_time", sa.String(length=10000), nullable=False)
        )
        batch_op.alter_column(
            "timezone",
            existing_type=sa.INTEGER(),
            type_=sa.String(length=10),
            existing_nullable=False,
        )
        batch_op.drop_column("schedule")
        batch_op.drop_column("preferred_times")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("availability_schedule", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "preferred_times",
                postgresql.JSON(astext_type=sa.Text()),
                autoincrement=False,
                nullable=False,
            )
        )
        batch_op.add_column(
            sa.Column(
                "schedule",
                postgresql.JSON(astext_type=sa.Text()),
                autoincrement=False,
                nullable=False,
            )
        )
        batch_op.alter_column(
            "timezone",
            existing_type=sa.String(length=10),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )
        batch_op.drop_column("availability_time")

    # ### end Alembic commands ###
