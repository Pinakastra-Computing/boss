"""Add rates model

Revision ID: 2b500992762
Revises: 514c4c54871
Create Date: 2015-06-09 23:22:46.980412

"""

# revision identifiers, used by Alembic.
revision = '2b500992762'
down_revision = '514c4c54871'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('billing_rate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('unit', sa.String(length=32), nullable=True),
    sa.Column('rate', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('billing_rate')
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass

