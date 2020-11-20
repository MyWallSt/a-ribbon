"""empty message

Revision ID: 04bebedb389c
Revises: 6c6a27e9a97d
Create Date: 2020-11-20 11:14:53.981353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04bebedb389c'
down_revision = '6c6a27e9a97d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stripe_checkout_session',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('gifter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gifter_id'], ['gifter.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('session_id')
    )
    with op.batch_alter_table('giftee', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('giftee', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    op.drop_table('stripe_checkout_session')
    # ### end Alembic commands ###
