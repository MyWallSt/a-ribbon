"""empty message

Revision ID: e6debb79271e
Revises: 2d4f5b21b841
Create Date: 2020-12-15 14:57:30.797294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6debb79271e'
down_revision = '2d4f5b21b841'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('giftee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('giftee', schema=None) as batch_op:
        batch_op.drop_column('test')

    # ### end Alembic commands ###
