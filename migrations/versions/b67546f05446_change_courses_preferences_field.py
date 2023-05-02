"""change courses_preferences field

Revision ID: b67546f05446
Revises: 64accb1b7221
Create Date: 2023-04-23 18:17:48.779433

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b67546f05446'
down_revision = '64accb1b7221'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('availability_schedule', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('permission', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('study_preferences', schema=None) as batch_op:
        batch_op.alter_column('courses_preferences',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=10)),
               type_=sa.String(length=500),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('user_information', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('user_information', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('study_preferences', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('courses_preferences',
               existing_type=sa.String(length=500),
               type_=postgresql.ARRAY(sa.VARCHAR(length=10)),
               existing_nullable=False)

    with op.batch_alter_table('permission', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('availability_schedule', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###