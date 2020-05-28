import { Component, OnInit } from '@angular/core';
import { ActorsService, Actor } from '../../services/actors.service';
import { ModalController } from '@ionic/angular';
import { ActorFormComponent } from './actor-form/actor-form.component';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-actor-menu',
  templateUrl: './actor-menu.page.html',
  styleUrls: ['./actor-menu.page.scss'],
})
export class ActorMenuPage implements OnInit {
  Object = Object;

  constructor(
    private auth: AuthService,
    private modalCtrl: ModalController,
    public actors: ActorsService,
    ) { }

  ngOnInit() {
    this.actors.getActors();
  }

  async openForm(activeactor: Actor = null) {
    if (!this.auth.can('get:actors')) {
      return;
    }

    const modal = await this.modalCtrl.create({
      component: ActorFormComponent,
      componentProps: { actor: activeactor, isNew: !activeactor }
    });

    modal.present();
  }

}
