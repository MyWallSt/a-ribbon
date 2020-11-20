"""empty message

Revision ID: d197a48c95b6
Revises: a74ef5ad9f0f
Create Date: 2020-11-20 12:01:42.580316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd197a48c95b6'
down_revision = 'a74ef5ad9f0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stripe_checkout_session', schema=None) as batch_op:
        batch_op.drop_constraint('stripe_checkout_session_session_id_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stripe_checkout_session', schema=None) as batch_op:
        batch_op.create_unique_constraint('stripe_checkout_session_session_id_key', ['session_id'])

    # ### end Alembic commands ###